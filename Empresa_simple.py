ingresos = float(input("Digite los ingresos del comprador: "))
costo_casa = float(input("Digite el costo de la casa: "))

if ingresos >= 80000:
    pie = costo_casa * 0.15
    pagos_mensuales = (costo_casa - pie) / 120  # 10 años = 10*12 meses
    print(f"El comprador debe pagar un pie de ${pie} y ${pagos_mensuales:.2f} mensualmente.")
else:
    pie = costo_casa * 0.30
    pagos_mensuales = (costo_casa - pie) / 84  # 7 años = 7*12 meses
    print(f"El comprador debe pagar un pie de ${pie} y ${pagos_mensuales:.2f} mensualmente.")
    #este código posee estructura simple