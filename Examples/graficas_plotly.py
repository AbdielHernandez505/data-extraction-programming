from tkinter.messagebox import showerror

import plotly.express as px


def graficas():
    df = px.data.gapminder()
    df_2007 = df[df.year == 2007]
    top = df_2007.sort_values("lifeExp", ascending=False).head(10)
    fig_barras = px.bar(
        top,
        x="country",
        y="lifeExp",
        color = "continent",
        title="Top 10 paises con mayor Esperanza de vida 2007"
    )

    df_mex = df[df.country == "Mexico"]
    fig_line = px.line(
        df_mex,
        x="year",
        y="lifeExp",
        title = "Esperanza de VIda en Mexico"
    )


    fig_line_paises = px.line(
        df[df.country.isin(["Mexico", "China", "United States"])],
        x="year",
        y="lifeExp",
        color = "country",
        title="Comparacion entre paises"
    )

    fig_histograma = px.histogram(
        df_2007,
        x = "lifeExp",
        nbins = 20,
        title = "Distribucion de Esperanza de Vida 2007"
    )

    fig_box = px.box(
        df_2007,
        x = "continent",
        y = "lifeExp",
        color = "continent",
        hover_name="country",
        title = "Esperanza de Vida entre continentes"
    )

    pop_continent = df_2007.groupby(["continent"]).sum().reset_index()
    fig_pie = px.pie(
        pop_continent,
        names = "continent",
        values = "pop",
        title = "Porcentaje poblacion por Continente"
    )

    fig_scatter = px.scatter(
        df_2007,
        x = "gdpPercap",
        y = "lifeExp",
        color = "continent",
        size = "pop",
        hover_name = "country",
        title = "PIB vs Esperanza de Vida 2007",
        log_x = True,
        log_y = True
    )
    fig_evolution = px.scatter(
        df,
        x="gdpPercap",
        y="lifeExp",
        color="continent",
        size="pop",
        hover_name="country",
        title="Evolucion mundial",
        animation_frame="year",
        log_x = True,
        log_y = True
    )

    fig_evolution.update_layout(
        template="plotly_dark",
    )



    fig_evolution.show()

    # fig_scatter.show()
    # fig_pie.show()
    # fig_box.show()
    # fig_histograma.show()
    # fig_line_paises.show()
    # fig_line.show()
    # fig_barras.show()

if __name__ == "__main__":
    graficas()

