import minecraft_launcher_lib
import subprocess

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
minecraft_directory.replace('minecraft', 'FLauncher')

print('by https://tg.me/farel106')


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, filling_symbol='█'):
    percent = round(100 * (iteration / float(total)), decimals)

    filled_length = int(length * iteration // total)

    bar = filling_symbol * filled_length + '-' * (length - filled_length)

    print(f'\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')

    if iteration == total:
        print()


callback = {
    "setStatus": print,
    "setProgress": lambda value: print_progress_bar(value, 100),
    "setMax": lambda text: print('New max: ', text),
}

minecraft_launcher_lib.install.install_minecraft_version(versionid='1.19.3', minecraft_directory=minecraft_directory, callback=callback)
