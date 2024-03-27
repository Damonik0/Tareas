ingresos = float(input("Ingrese los ingresos del comprador: "))
costo_casa = float(input("Ingrese el costo de la casa: "))

if ingresos >= 80000:
    pie = costo_casa * 0.15
    pagos_mensuales = (costo_casa - pie) / 120  # 10 años = 10*12 meses
    print(f"El comprador debe pagar un pie de ${pie} y ${pagos_mensuales:.2f} por cada pago mensual.")
else:
    if ingresos < 80000:
        pie = costo_casa * 0.30
        pagos_mensuales = (costo_casa - pie) / 84  # 7 años = 7*12 meses
        print(f"El comprador debe pagar un pie de ${pie} y ${pagos_mensuales:.2f} por cada pago mensual.")
        #este código posee una estructura doble