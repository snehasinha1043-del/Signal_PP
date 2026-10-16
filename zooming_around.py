if spectrum_view == "Around Signal":
        compare_fig.update_xaxes(
            range=[
                max(0, frequency - 500),
                min(sampling_frequency / 2, frequency + 500)
            ]
        )
