def ensure_bookmark_path(state, path):
    submap = state
    for path_component in path:
        if submap.get(path_component) is None:
            submap[path_component] = {}

        submap = submap[path_component]
    return state

def write_bookmark(state, tap_stream_id, key, val):
    state = ensure_bookmark_path(state, ['bookmarks', tap_stream_id])
    state['bookmarks'][tap_stream_id][key] = val
    return state

def get_bookmark(state, tap_stream_id, key):
    return state.get('bookmarks', {}).get(tap_stream_id, {}).get(key)

def set_offset(state, tap_stream_id, offset_key, offset_value):
    state = ensure_bookmark_path(state, ['bookmarks', tap_stream_id, "offset", offset_key])
    state['bookmarks'][tap_stream_id]["offset"][offset_key] = offset_value
    return state

def clear_offset(state, tap_stream_id):
    state = ensure_bookmark_path(state, ['bookmarks', tap_stream_id, "offset"])
    state['bookmarks'][tap_stream_id]["offset"] = {}
    return state

def get_offset(state, tap_stream_id):
    return state.get('bookmarks', {}).get(tap_stream_id, {}).get("offset")

def set_currently_syncing(state, tap_stream_id):
    state['currently_syncing'] = tap_stream_id
    return state

def get_currently_syncing(state):
    return state.get('currently_syncing')
