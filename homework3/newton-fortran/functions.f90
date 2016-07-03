module functions

  real(kind=8), parameter :: PI = 3,14159265358979323846

contains

  real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

  end function f_sqrt


  real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

  end function fprime_sqrt


  real(kind=8) function myfunc(x)
    implicit none
    real(kind=8), intent(in) :: x

    myfunc = x * cos(PI * x) - 1 + 0.6 * x**2

  end function myfunc

  real(kind=8) function myfunc_prima(x):
    implicit none
    real(kind=8), intent(in) :: x

    myfunc_prima = cos(PI * x) - PI * x * sin(PI * x) + 1.2 * x

  end function myfunc_prima
  
end module functions
