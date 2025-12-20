class RootFinder:
    """
    Class to find Square Root and Nth Root using
    Binary Search, Newton-Raphson, and Hybrid methods.
    """

    # ----------------------------------------------------
    # 1. Square Root using Binary Search
    # ----------------------------------------------------
    @staticmethod
    def sqrt_binary(N, eps=1e-7):
        """
        Parameters:
        N   : The number whose square root is to be computed (non-negative).
        eps : Precision/tolerance for stopping the binary search (default 1e-7).

        Returns:
        Approximate square root of N as float.
        """
        # Determine search interval
        if N < 1:
            low, high = 0, 1   # for numbers between 0 and 1
        else:
            low, high = 0, N   # for numbers >= 1

        # Binary search loop
        while high - low > eps:
            mid = (low + high) / 2
            if mid * mid > N:
                high = mid
            else:
                low = mid

        # Return average of low and high as approximate root
        return (low + high) / 2

    # ----------------------------------------------------
    # 2. Nth Root using Binary Search
    # ----------------------------------------------------
    @staticmethod
    def nth_root_binary(N, n, eps=1e-7):
        """
        Parameters:
        N   : The number whose nth root is to be computed (positive).
        n   : Degree of the root (integer >= 2).
        eps : Precision/tolerance for stopping the binary search.

        Returns:
        Approximate nth root of N as float.
        """
        if N < 1:
            low, high = 0, 1
        else:
            low, high = 0, N

        while high - low > eps:
            mid = (low + high) / 2
            if mid ** n > N:
                high = mid
            else:
                low = mid

        return (low + high) / 2

    # ----------------------------------------------------
    # 3. Square Root using Newton-Raphson
    # ----------------------------------------------------
    @staticmethod
    def sqrt_newton(N, eps=1e-7):
        """
        Parameters:
        N   : The number whose square root is to be computed (non-negative).
        eps : Precision/tolerance for stopping Newton-Raphson iterations.

        Returns:
        Approximate square root of N as float.
        """
        x = N
        while True:
            nx = 0.5 * (x + N / x)
            if abs(nx - x) < eps:
                return nx
            x = nx

    # ----------------------------------------------------
    # 4. Nth Root using Newton-Raphson
    # ----------------------------------------------------
    @staticmethod
    def nth_root_newton(N, n, eps=1e-7):
        """
        Parameters:
        N   : The number whose nth root is to be computed (positive).
        n   : Degree of the root (integer >= 2).
        eps : Precision/tolerance for stopping Newton-Raphson iterations.

        Returns:
        Approximate nth root of N as float.
        """
        x = N
        while True:
            nx = ((n - 1) * x + N / (x ** (n - 1))) / n
            if abs(nx - x) < eps:
                return nx
            x = nx

    # ----------------------------------------------------
    # 5. Hybrid Method (Binary → Newton) for Square Root
    # ----------------------------------------------------
    @staticmethod
    def sqrt_hybrid(N, eps=1e-7):
        """
        Parameters:
        N   : The number whose square root is to be computed.
        eps : Precision/tolerance for Newton-Raphson refinement.

        Returns:
        Approximate square root of N as float.
        """
        # Step 1: Binary search narrowing
        low, high = 0, N if N >= 1 else 1
        for _ in range(40):
            mid = (low + high) / 2
            if mid * mid > N:
                high = mid
            else:
                low = mid

        x = (low + high) / 2

        # Step 2: Newton refinement
        while True:
            nx = 0.5 * (x + N / x)
            if abs(nx - x) < eps:
                return nx
            x = nx

    # ----------------------------------------------------
    # 6. Hybrid Method (Binary → Newton) for Nth Root
    # ----------------------------------------------------
    @staticmethod
    def nth_root_hybrid(N, n, eps=1e-7):
        """
        Parameters:
        N   : The number whose nth root is to be computed.
        n   : Degree of the root (integer >= 2).
        eps : Precision/tolerance for Newton-Raphson refinement.

        Returns:
        Approximate nth root of N as float.
        """
        # Step 1: Binary search narrowing
        low, high = 0, N if N >= 1 else 1
        for _ in range(40):
            mid = (low + high) / 2
            if mid ** n > N:
                high = mid
            else:
                low = mid

        x = (low + high) / 2

        # Step 2: Newton refinement
        while True:
            nx = ((n - 1) * x + N / (x ** (n - 1))) / n
            if abs(nx - x) < eps:
                return nx
            x = nx
