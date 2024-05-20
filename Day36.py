def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    # Tạo một danh sách đánh dấu tất cả các số từ 0 đến n là nguyên tố
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 và 1 không phải là số nguyên tố

    # Sử dụng Sieve of Eratosthenes
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    # Trả về kết quả kiểm tra số n
    return sieve[n]

if __name__ == "__main__":
    print(is_prime(5))
    print(is_prime(5.0))