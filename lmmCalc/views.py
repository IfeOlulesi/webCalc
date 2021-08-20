from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import math
import numpy as np


def backLogic(inputDict):
    response = {
        "alphas": [],
        "betas": [],
        "consistency": "",
        "error": "",
        "isExplicit": "",
        "isConsistent": "",
        "zeroStability": "",
        "errorConstant": 0,
        "order": "",
        "fatalError": "",
    }

    n = 0
    m = 0
    ans = []
    coefficients = []
    coefficients2 = []

    d = []
    k = int(inputDict["alpha-total"][0])
    z = float(2)
    w = float(z - 1)
    z_fact = math.factorial(z)
    w_fact = math.factorial(w)

    for p in range(0, int(k) + 1):

        Y = inputDict[f"alpha-{p}"]
        Y = float(eval(Y))
        # print("α" + str(n), "=", Y)
        coefficients.append(Y)
        const1 = sum(coefficients)
        # print()

        F = inputDict[f"beta-{p}"]
        F = float(eval(F))

        # print("β" + str(m), "=", F)
        coefficients2.append(F)
        # print()

        # To check for consistency
        value = n * Y - F
        ans.append(value)
        my_rounds = [round(numb, 4) for numb in ans]
        const2 = sum(my_rounds)

        # To check for the error constant and order for n = 2
        c = ((1 / z_fact) * (n ** z) * Y) - ((1 / w_fact) * (n ** w) * F)
        d.append(c)
        Error_const = sum(d)

        n += 1
        m += 1

    # print(f"Coefficient array: {coefficients}")
    # print(f"Coefficient 2 array: {coefficients2}")
    response["alphas"] = coefficients
    response["betas"] = coefficients2

    # print()
    # print()
    const2 = round(sum(my_rounds), 1)

    # print("Test for Convergence")
    # print()

    # print("Test for Consistency")
    # print("Consistency =", const1)
    # print("Error =", const2)

    response["consistency"] = const1
    response["error"] = const2

    if F == 0:
        # print("It's an explicit method")
        response["isExplicit"] = True
    else:
        # print("It's an implicit method")
        response["isExplicit"] = False

    if const1 == const2:
        # print("The method is consistent")
        response["isConsistent"] = True
    else:
        # print("This method is not consistent")
        response["isConsistent"] = False
    # print()
    # print()
    # To check for zero stability
    # coefficients = np.squeeze(coefficients)
    p = np.poly1d(coefficients)
    roots = p.roots
    # print(roots)

    if roots.all() <= 1:
        # print("The method is zero stable because |r| <= 1")
        response["zeroStability"] = True
    else:
        # print("The method is not zero stable")
        response["zeroStability"] = False

    print()

    Error_const = round(Error_const, 1)

    if Error_const == 0:
        count = 0
        while Error_const == 0:
            n = 0
            e = []
            z += 1
            w = z - 1
            z_fact = math.factorial(z)
            w_fact = math.factorial(w)

            for q in range(0, int(k) + 1):
                c = ((1 / z_fact) * (n ** z) * (coefficients[n])) - (
                    (1 / w_fact) * (n ** w) * (coefficients2[n])
                )
                e.append(c)
                my_round1 = [round(num, 4) for num in e]
                Error_const2 = sum(my_round1)
                n += 1
            count += 1

            Error_const2 = round(sum(my_round1), 3)

            if Error_const != Error_const2:
                break

        # print("Test for error constant and order")
        # print("The error constant is", Error_const2)
        # print("The method is of order", count + 1)

        response["errorConstant"] = Error_const2
        response["order"] = count + 1

        # print(response)

    else:
    #     print(f"=" * 40)
    #     print("Error: The wrong values were entered")
    #     print(f"The variable error_const is: {Error_const}.")

        response["fatalError"] = True

    return response


# Create your views here.


def index(request):
    return render(request, "lmmCalc/index.html")


def answer(request):
    response = backLogic(request.POST)
    print(response)
    return render(request, "lmmCalc/result.html", response)