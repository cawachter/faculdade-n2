tempoExperiencia = 6

if tempoExperiencia <= 2:
    print("Nível de conhecimento júnior")

elif tempoExperiencia > 2 and tempoExperiencia <= 5:
    print("Nível de conhecimento pleno")

else:
    print("Nível de conhecimento sênior")


# TempoExperiencia = 2 ou 5 não estava previsto no exercício. Iria cair no else de conhecimento Senior.
# Por isso tomei a liberade de colocar tempoExperiencia = 2 para junior e tempoExperiencia = 5 para pleno.