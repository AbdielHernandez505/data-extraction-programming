import streamlit as st
import plotly.express as px

def render():
    st.set_page_config(
        page_title="Primer Dashboard",
        layout="wide",
    )

    df = px.data.gapminder()

    st.title("Primer Dashboard")

    st.sidebar.title("Filtros")

    continente = st.sidebar.multiselect("Continente", df.continent.unique())
    year = st.sidebar.slider("Year", df.year.min(), df.year.max(), step=5, value=2002)

    df_filtrado = df[(df.year == year) & (df.continent.isin(continente))]

    st.markdown("### INDICADORES 😐")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Paises", df_filtrado.country.nunique())
    col2.metric("Poblacion", df_filtrado["pop"].sum())
    col3.metric("PIB Promedio", round(df_filtrado.gdpPercap.mean(), 2))
    col4.metric("Esperanza de vida Promedio", round(df_filtrado.lifeExp.mean(), 2))

    st.markdown("")

    col1, col2 = st.columns(2)

    fig1 = px.scatter(df_filtrado,
                      x="gdpPercap",
                      y="lifeExp",
                      color="continent",
                      size="pop",
                      hover_name="country",
                      title="PIB vs Esperanza de Vida 2007",
                      )
    col1.plotly_chart(fig1)

    top = df_filtrado.sort_values("lifeExp", ascending=False).head(10)

    fig2 = px.bar(top, x="country", y="lifeExp", color="continent", title = "top paises")

    col2.plotly_chart(fig2)

    st.markdown("")

    with st.expander("Ver datos"):
        st.dataframe(df)

render()