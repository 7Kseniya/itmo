import re 

#task1
#';<{|'
strings= (':</;<{|=<(8<{P8-)=</;<);<{|:<\:-{\8<PX-PX<{O;<{|;<{P;<O8-PX<',
          'X-P;<{|;<{|8-|X<P:<|;<);<PX-(;<{|;<{/=-{\8<{\8<|X-(;-(;<{|X-/X-\=-|8<',
          '</X-P;<|:<P:<{(8</:<{/8-OX<(8-{)X<(:-O8<{|X</;<{\;-(=',
          '<{O;<{\X-{P:<P:<|:-(X</=<{/=-{O=<(=-{O=<|;<O;-/'
          '8<);<{|8<{P=<|;-PX-{(8-|=<)8<);<\:<{/;<PX<')

for test_string in strings:
    check_by_re = len(re.findall(r';<\{\|',test_string))
    check_by_count = test_string.count(';<{|')
    print(f'string contains {check_by_re} smiles')
    if check_by_re == check_by_count:
        print('correct')
    else:
        print('incorrect')
