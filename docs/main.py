from build import build_all

def parse_cmd(cmd):
    words = cmd.split()
    if words[0] == 'build':
        if len(words) == 2:
            if words[1] == 'all':
                build_all()
            else:
                print('ignored ...')

if __name__ == '__main__':
    isOn = 1
    while isOn:
        cmd = input('\n>>> ').strip()
        if cmd == 'exit':
            isOn = 0
            print('exiting ...')
        else:
            parse_cmd(cmd)


