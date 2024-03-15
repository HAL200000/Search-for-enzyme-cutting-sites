def is_bio_palindrome(s):
    # 核苷酸及其互补对应关系
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # 生成互补序列
    complement_seq = ''.join(complement[nuc] for nuc in s)

    # 根据生物学规则检查序列是否为回文序列
    return s == complement_seq[::-1]


# 定义一个函数，找出给定序列中长度为4、6、8的回文序列
def find_bio_palindromic_sequences(sequence):
    results = []
    for length in [4, 6, 8]:
        for i in range(len(sequence) - length + 1):
            substring = sequence[i:i + length]
            if is_bio_palindrome(substring):
                results.append((substring, i + 1, i + length))
    return results


# 定义一个函数，找出特定序列'GCTNAGC'，其中'N'可以是任何核苷酸
def find_specific_sequence(sequence):
    results = []
    for i in range(len(sequence) - 6):
        if sequence[i:i + 3] == 'GCT' and sequence[i + 4:i + 7] == 'AGC':
            results.append((sequence[i:i + 7], i + 1, i + 7))
    return results


# 定义一个函数，处理fasta文件，并在每个基因序列中找到所有的酶切位点
def process_fasta_file(file_path):
    with open(file_path, 'r') as file:
        sequences = []
        current_seq = ''
        current_desc = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:
                    sequences.append((current_desc, current_seq))
                    current_seq = ''
                current_desc = line[1:]
            else:
                current_seq += line
        if current_seq:
            sequences.append((current_desc, current_seq))

    # 在每个基因序列中找出回文序列和特定序列
    for desc, seq in sequences:
        palindromic_sequences = find_bio_palindromic_sequences(seq)
        specific_sequences = find_specific_sequence(seq)
        total_sites = len(palindromic_sequences) + len(specific_sequences)

        print(f"描述: {desc}")
        print(f"总酶切位点数: {total_sites}")
        for site in palindromic_sequences + specific_sequences:
            print(f"位点: {site[0]}, 长度: {len(site[0])}, 起始: {site[1]}, 结束: {site[2]}")


process_fasta_file("data/sequence.fasta")
