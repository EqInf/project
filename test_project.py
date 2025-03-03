import pytest
from project import calculate_bmr, calculate_tdee, macronutrient_distribution

# def test_calculate_bmr was done by ChatGPT and was used as an example of proper logic. Following functions, which are test_calculate_tdee and test_macronutrient_distribution were done on our own.
def test_calculate_bmr():
    assert calculate_bmr(70, 175, 25, "male") == pytest.approx(1673.75, rel=1e-2)
    assert calculate_bmr(60, 160, 30, "female") == pytest.approx(1289.0, rel=1e-2)
    with pytest.raises(ValueError):
        calculate_bmr(70, 175, 25, "unknown")

def test_calculate_tdee():
    assert calculate_tdee(1700, "moderate") == pytest.approx(2635, rel=1e-2)
    assert calculate_tdee(1500, "sedentary") == pytest.approx(1800, rel=1e-2)
    with pytest.raises(ValueError):
        calculate_tdee(1700, "super active")

def test_macronutrient_distribution():
    result = macronutrient_distribution(2500, "gain")
    assert result["calories"] == pytest.approx(3000, rel=1e-2)
    assert result["protein"] == pytest.approx((3000 * 0.3) / 4, rel=1e-2)
    assert result["carbs"] == pytest.approx((3000 * 0.5) / 4, rel=1e-2)
    assert result["fats"] == pytest.approx((3000 * 0.2) / 9, rel=1e-2)
    
    with pytest.raises(ValueError):
        macronutrient_distribution(2500, "bulk")
