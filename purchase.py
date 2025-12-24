import pandas as pd
import streamlit as st
import joblib
import warnings

warnings.filterwarnings("ignore")


try:
    logistic_model = joblib.load(r"purchased.joblib")
    st.title("Product is purchased or not")
    st.write("Logistic model is loaded succesfully with solver is liblinear ")
    st.markdown(
        """if "0" means not purchase || if "1" means product is purchased """
    )  # noqa: ignore
    st.success("Model loaded success")
    st.balloons()
    st.sidebar.write("Choose the input parameters")
    with st.sidebar.form(key="input parameters"):
        with st.sidebar:
            Age = st.number_input("AGE", min_value=18, max_value=90, value=45)
            Ets = st.number_input(
                "ETS", min_value=10000, max_value=10000000, value=83457
            )
            Gen = st.number_input(
                "GEN",
                min_value=1,
                max_value=2,
                value=1,
                help="1 is male and 2 is female",
            )
            submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.success("Form is submitted succesfully ....!")
        model_dict = {"Age": Age, "Ets": Ets, "gen": Gen}
        df4 = pd.DataFrame(data=model_dict, index=[0])

        preditations = logistic_model.predict(df4)
        st.code(f"Result is : --> {abs(preditations[0])}")
        st.header("Barchart")
        st.bar_chart(df4)
        st.subheader("Scatter plot")
        st.scatter_chart(df4)
        st.table(df4)
        st.data_editor(df4)
    else:
        st.warning("Form is not submitted  ....! ")

except Exception as e:
    st.warning(f"{str(e)}")
    st.code(f"{str(e)}", language="Python")
else:
    print("no errors in the code")
    st.info("No errors in the code ")
finally:
    st.success("final block is executed succsully")
