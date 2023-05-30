from dataclasses import dataclass
from statsmodels.stats.power import (
    tt_ind_solve_power,
    FTestAnovaPower,
    GofChisquarePower,
)


def calculate_anova_sample_size(effect_size, alpha, power, k_groups):
    return FTestAnovaPower().solve_power(
        effect_size=effect_size, nobs=None, alpha=alpha, power=power, k_groups=k_groups
    )


def calculate_chi_squared_sample_size(alpha, power, effect_size, n_bins):
    return GofChisquarePower().solve_power(
        effect_size=effect_size, nobs=None, alpha=alpha, power=power, n_bins=n_bins
    )


@dataclass
class test_var:
    name: str
    id: str
    type: str
    value: any


@dataclass
class TestsBase:
    label: str
    value: str
    vars: list[test_var]
    func: callable



class t_test(TestsBase):
    label = "T-Test"
    value = "t_test"
    vars = [
        test_var("Significance level", "alpha", "number", 0.05),
        test_var("Power", "power", "number", 0.8),
        test_var("Effect size", "effect_size", "number", 0.2),
        test_var("Ratio", "ratio", "number", 1)
        # test_var("Tails", "t_tails"),
    ]
    func = tt_ind_solve_power


class anova(TestsBase):
    label = "ANOVA"
    value = "anova"
    vars = [
        test_var("Significance level", "alpha", "number", 0.05),
        test_var("Power", "power", "number", 0.8),
        test_var("Effect size", "effect_size", "number", 0.2),
        test_var("Number of groups", "k_groups", "number", 3),
    ]
    func = calculate_anova_sample_size


class chi_squared(TestsBase):
    label = "Chi-Squared"
    value = "chisq"
    vars = [
        test_var("Significance level", "alpha", "number", 0.05),
        test_var("Power", "power", "number", 0.8),
        test_var("Effect size", "effect_size", "number", 0.2),
        test_var("Number of cells", "n_bins", "number", 4),
    ]
    func = calculate_chi_squared_sample_size

@dataclass
class DataInterface:
    tests = {
        t_test.value: t_test,
        anova.value: anova,
        chi_squared.value: chi_squared,
    }
