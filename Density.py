def density(pop, sup):
    return pop/sup
# Superfice km2
Haiti = density(12000000, 27250)
a = "The density of"
Canada = density (39000000, 9985000)
Qatar = density (2688000, 11581)
Poland = density (38000000, 312696)
print(" "+ a + " Haiti is " + str(round(Haiti, 2)),"\n",
      a + " Canada is " + str(round(Canada, 2)), "\n",
    a + " Qatar is " + str(round(Qatar, 2)), "\n",
    a + " Poland is " + str(round(Poland, 2)))
