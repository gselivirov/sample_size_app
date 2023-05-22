from dataclasses import dataclass


@dataclass
class test_var:
    name: str
    id: str


@dataclass
class TestsBase:
    label: str
    value: str
    vars: list[test_var]


class t_test(TestsBase):
    label = "t-test"
    value = "t_test"
    vars = [
        test_var("Significance level", "t_alpha"),
        test_var("Power", "t_beta"),
        test_var("Effect size", "t_delta"),
        test_var("Tails", "t_tails")
    ]


class anova(TestsBase):
    label = "ANOVA"
    value = "anova"
    vars = [test_var("anova1", "var_a_1")]
