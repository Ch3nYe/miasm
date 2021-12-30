use pyo3::prelude::*;

#[pyfunction]
pub fn myfunc_return_first_char(s: &str) -> &str {
    &s[..1]
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyclass]
struct DummyClass {}

#[pymethods]
impl DummyClass {
    #[staticmethod]
    fn get_42() -> PyResult<usize> {
        Ok(42)
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(myfunc_return_first_char, m)?)?;
    m.add_class::<DummyClass>()?;
    m.add("fourtytwo", 42)?;

    Ok(())
}
// ref maturin: build rust to wheel:: https://github.com/PyO3/maturin
// ref pyo3: use rust in python:: https://pyo3.rs/v0.15.1/index.html