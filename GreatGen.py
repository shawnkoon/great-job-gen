NUM_TO_ENG_MAP = {
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
}


def main():
  list_kwargs = ['Great Job today']

  for number in range(1, 15):
    if number == 1:
      list_kwargs.append('yesterday')
    elif number in range(2, 10):
      list_kwargs.append(f'{NUM_TO_ENG_MAP[number]} days ago')
    else:
      list_kwargs.append(f'{number} days ago')
  
  list_kwargs.append('and tomorrow 👍🏼')

  print_msg(list_kwargs)


def print_msg(*args):
  delimiter = ', '
  print(delimiter.join(*args))

if __name__ == "__main__":
  main()