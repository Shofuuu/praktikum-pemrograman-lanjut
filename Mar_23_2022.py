#!/usr/bin/python3

def draw_table(dict_data):
    dict_key = list(dict_data.keys())
    dict_value = list(dict_data.values())

    longest_word = [1, 1]
    for i in range(len(dict_key)):
        if len(dict_key[i]) > longest_word[0]:
            longest_word[0] = len(dict_key[i])
    for i in range(len(dict_value)):
        str_dict_val = str(dict_value[i])
        if len(str_dict_val) > longest_word[1]:
            longest_word[1] = len(str_dict_val)

    longest_word[0] += 2
    longest_word[1] += 2

    for x in range(len(dict_key)):
        print('+', '-'*longest_word[0], '+', sep='', end='')
        print('-'*longest_word[1], '+', sep='')
        print('| ', dict_key[x], ' '*(longest_word[0] + (longest_word[0]-len(dict_key[x]))), '\b'*(longest_word[0]+1), sep='', end='')
        if type(dict_value[x]) == int or type(dict_value[x]) == float:
            str_dict_val = ('Rp' + str('{:,}'.format(dict_value[x]*1000)))
            print('| ', str_dict_val, ' '*(longest_word[1] + (longest_word[1]-len(str_dict_val))), '\b'*(longest_word[1]+1), '|', sep='')
        else:
            print('| ', dict_value[x], ' '*(longest_word[1] + (longest_word[1]-len(dict_value[x]))), '\b'*(longest_word[1]+1), '|', sep='')

        if x == len(dict_key)-1:
            print('+', '-'*longest_word[0], '+', sep='', end='')
            print('-'*longest_word[1], '+', sep='')

if __name__ == '__main__':
    dict_vegetables_prices = {'Jenis Sayur': 'Harga Sayur', 'Bayam': 1.5, 'Terong': 2, 'Kubis': 3, 'Labu': 4, 'Brokoli': 4.5}
    dict_merged = {'Barang Belanjaan': 'Total yang Harus di Bayar'}
    draw_table(dict_vegetables_prices)

    while True:
        try:
            total = int(input('\nAda berapa jenis sayur (0 ahiri program)? '))
        except:
            print('\n[ERROR] Input harus berupa angka!')
            continue

        dict_vegetables_user = {}
        max_total = total

        if total == 0:
            break

        while total > 0:
            key_vegetables = input('  Nama sayur ['+str(max_total - total)+']: ')
            key_vegetables = key_vegetables.capitalize()
            last_key = ''

            if key_vegetables not in dict_vegetables_prices.keys():
                print('  Sayur tidak ada di daftar harga!')
            else:
                try:
                    value_vegetables = int(input('  Jumlah: '))
                except:
                    print('[ERROR] Input harus berupa angka!')
                    continue
                dict_vegetables_user.update({str(key_vegetables + ' ' + str(value_vegetables)): value_vegetables*dict_vegetables_prices[key_vegetables]})
                total -= 1

        key_str_merge = ''
        val_num_total = 0
        for key in dict_vegetables_user.keys():
            key_str_merge += key + (', ' if key != list(dict_vegetables_user.keys())[-1] else '')
        for val in dict_vegetables_user.values():
            val_num_total += val

        val_num_total = val_num_total - (val_num_total * (
            0.20 if val_num_total > 100 else(
                0.15 if val_num_total > 50 else(
                    0.10 if val_num_total > 20 else 0
                )
            )
        ))

        dict_merged.update({key_str_merge: val_num_total})
        draw_table(dict_merged)
    
    print('\nTerima kasih telah berbelanja di toko sayur kami!')