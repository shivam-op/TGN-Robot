if query.data == 'channelblock':
        record = GroupRepository.SENDER_CHAT_BLOCK
        row = group['sender_chat_block']
        if row == 1:
            update_db_settings(update, record, True)

