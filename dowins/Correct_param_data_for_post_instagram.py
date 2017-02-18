
def make_post_data(user_id, cursor):
    """
    Make correct dictonary query for post_data
    """
    dict_post = {'q': "ig_user(" + user_id + ") { media.after(" + cursor + ", 12) {" +
    "count," +
    "nodes {" +
    "  __typename," +
    "  caption," +
    "  code," +
    "  comments {" +
    "    count" +
    "  }," +
    "  comments_disabled," +
    "  date," +
    "  dimensions {" +
    "    height," +
    "    width" +
    "  }," +
    "  display_src," +
    "  id," +
    "  is_video," +
    "  likes {" +
    "    count" +
    "  }," +
    "  owner {" +
    "    id" +
    "  }," +
    "  thumbnail_src," +
    "  video_views" +
    "}," +
    "page_info" +
    "}" +
    " }"
                 }
    dict_post.update({'ref': 'users::show'})
    return dict_post
