import dash
import dash_bootstrap_components as dbc
from dash import dcc, html


def render_copy(result: int, selected_test: str, variables: dict) -> list:
    match selected_test:
        case "t_test":
            return [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Results and Interpretation", class_name="text-center"
                        ),
                        dbc.CardBody(
                            [
                                html.H5(
                                    result, className="text-center", id="result_header"
                                ),
                                html.Div(id="size"),
                                html.Div(
                                    [
                                        html.P(
                                            f"Estimated sample size for the first group is {result}, and the ratio between the first and second groups is {variables['ratio']}. "
                                        ),
                                        html.P(
                                            f"In total, you would need {int(result + result * variables['ratio'])} participants. "
                                        ),
                                        html.P(
                                            f"The probability of a Type 1 error is {variables['alpha']}, and the probability of a Type 2 error is {round(1 - variables['power'], 2)}. "
                                        ),
                                        html.P(
                                            f"The sensitivity is {variables['effect_size']} Cohen's d. "
                                        ),
                                        html.H6(
                                            "Additional Information",
                                            className="text-center",
                                        ),
                                        html.P(
                                            f"Cohen's d is a measure of the standardized effect size, which quantifies the difference between the means of the two groups. A Cohen's d of 0.5 indicates a medium effect size."
                                        ),
                                        html.P(
                                            f"A Type 1 error refers to rejecting the null hypothesis when it is actually true, and its probability is typically set at 0.05."
                                        ),
                                        html.P(
                                            f"A Type 2 error refers to failing to reject the null hypothesis when it is actually false, and its probability is calculated as 1 - Power, which is typically set at 0.8."
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    color="dark",
                    outline=True,
                ),
            ]
        case "anova":
            return [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Results and Interpretation", class_name="text-center"
                        ),
                        dbc.CardBody(
                            [
                                html.H5(
                                    result, className="text-center", id="result_header"
                                ),
                                html.Div(id="size"),
                                html.Div(
                                    [
                                        html.P(
                                            f"Estimated sample size for the first group is {result}, and the total number if groups is {variables['k_groups']}. "
                                        ),
                                        html.P(
                                            f"In total, you would need {int(result * variables['k_groups'])} participants. "
                                        ),
                                        html.P(
                                            f"The probability of a Type 1 error is {variables['alpha']}, and the probability of a Type 2 error is {round(1 - variables['power'], 2)}. "
                                        ),
                                        html.P(
                                            f"The sensitivity is {variables['effect_size']} Cohen's f. "
                                        ),
                                        html.H6(
                                            "Additional Information",
                                            className="text-center",
                                        ),
                                        html.P(
                                            f"Cohen's f is a measure of the standardized effect size, which quantifies the difference between the means of the multiple groups. A Cohen's f of 0.5 indicates a medium effect size."
                                        ),
                                        html.P(
                                            f"A Type 1 error refers to rejecting the null hypothesis when it is actually true, and its probability is typically set at 0.05."
                                        ),
                                        html.P(
                                            f"A Type 2 error refers to failing to reject the null hypothesis when it is actually false, and its probability is calculated as 1 - Power, which is typically set at 0.8."
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    color="dark",
                    outline=True,
                ),
            ]
        case "chisq":
            return [
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Results and Interpretation", class_name="text-center"
                        ),
                        dbc.CardBody(
                            [
                                html.H5(
                                    result, className="text-center", id="result_header"
                                ),
                                html.Div(id="size"),
                                html.Div(
                                    [
                                        html.P(
                                            f"Estimated sample size is {result}. "
                                        ),
                                        html.P(
                                            f"The probability of a Type 1 error is {variables['alpha']}, and the probability of a Type 2 error is {round(1 - variables['power'], 2)}. "
                                        ),
                                        html.P(
                                            f"The sensitivity is {variables['effect_size']}"
                                        ),
                                        html.H6(
                                            "Additional Information",
                                            className="text-center",
                                        ),
                                        html.P(
                                            f"A Type 1 error refers to rejecting the null hypothesis when it is actually true, and its probability is typically set at 0.05."
                                        ),
                                        html.P(
                                            f"A Type 2 error refers to failing to reject the null hypothesis when it is actually false, and its probability is calculated as 1 - Power, which is typically set at 0.8."
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    color="dark",
                    outline=True,
                ),
            ]
