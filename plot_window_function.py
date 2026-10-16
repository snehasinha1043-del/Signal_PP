window_fig = go.Figure()

    window_fig.add_trace(
        go.Scatter(
            x=np.arange(samples),
            y=window_values,
            mode="lines",
            name="Window Function"
        )
    )

    window_fig.update_layout(
        title=f"{window} Window",
        xaxis_title="Sample Index",
        yaxis_title="Amplitude",
        template="plotly_dark"
    )

    st.plotly_chart(window_fig, use_container_width=True)
