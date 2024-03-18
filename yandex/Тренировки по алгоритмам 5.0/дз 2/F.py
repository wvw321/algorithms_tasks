def count(n, arr, a, b, k):
    if a / k == a // k:
        i = a // k - 1
    else:
        i = a // k

    if i > n:
        i = i % n

    max_result = arr[0 + i]
    max_result = max(max_result, arr[0 - i])
    count = 0

    for v in range(a, b + 1, k):
        if count < n:
            ind_pus = 0 + i + count
            ind_min = 0 - i - count

            if ind_pus > n - 1:
                ind_pus = ind_pus % n

            if ind_min < -n + 1:
                ind_min = ind_min % -n

            max_result = max(max_result, arr[ind_pus])
            max_result = max(max_result, arr[ind_min])
            count += 1
        else:
            break
    return max_result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    a, b, k = map(int, input().split())
    print(count(n, arr, a, b, k))

# for v in range(a, b + 1, k):
#     v_now = v
#     i = 0
#     while v_now > k:
#         i += 1
#         if i > n - 1:
#             i = 0
#         v_now -= k
#     max_result = max(max_result, arr[i])
#
#     v_now = v
#     i = 0
#     while v_now > k:
#         i -= 1
#         if i < -n + 1:
#             i = 0
#         v_now -= k
#     max_result = max(max_result, arr[i])
#
# print(max_result)
