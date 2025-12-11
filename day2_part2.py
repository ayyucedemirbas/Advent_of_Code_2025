def solve_day2_part2(input_data):
    input_data = input_data.replace('"', '').replace('\n', '').strip()
    ranges = input_data.split(',')
    
    total_sum = 0
    
    for r in ranges:
        if not r.strip():
            continue
        start_s, end_s = r.split('-')
        start = int(start_s)
        end = int(end_s)
        
        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)
            is_invalid = False
            
            for pat_len in range(1, length // 2 + 1):
                if length % pat_len == 0:
                    pattern = s_num[:pat_len]
                    multiplier = length // pat_len
                    if pattern * multiplier == s_num:
                        is_invalid = True
                        break
            
            if is_invalid:
                total_sum += num
                
    return total_sum

input_str = """
119-210,907313-1048019,7272640820-7272795557,6315717352-6315818282,42-65,2234869-2439411,1474-2883,33023-53147,1-15,6151-14081,3068-5955,65808-128089,518490556-518593948,3535333552-3535383752,7340190-7548414,547-889,34283147-34389716,44361695-44519217,607492-669180,7071078-7183353,67-115,969-1469,3636264326-3636424525,762682710-762831570,827113-906870,205757-331544,290-523,86343460-86510016,5536957-5589517,132876-197570,676083-793651,23-41,17920-31734,440069-593347
"""

print(solve_day2_part2(input_str))
