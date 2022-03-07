from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_disambiguation_keyboard(disambiguation_options):
   keyboard = []

   for option in disambiguation_options:
     new_option = [InlineKeyboardButton(option, callback_data='ERROR;DISAMBIGUATION;' + option)]
     keyboard.append(new_option)

   return InlineKeyboardMarkup(keyboard)
