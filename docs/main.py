from build import build_main_page, build_members_basic

def parse_cmd(cmd):
    words = cmd.split()
    if words[0] == 'build':
        if len(words) == 2:
            if words[1] == 'main':
                build_main_page()
            elif words[1] == 'members_basic':
                build_members_basic()
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


