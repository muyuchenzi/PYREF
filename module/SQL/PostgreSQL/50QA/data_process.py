from data_insert import db_connect


def data_add_column():
    get_data = db_connect()
    renameed_data = get_data.rename(columns={0: "name", 1: "订单数"})
    return renameed_data


def cmp_data_searcher():
    cmp_data = data_add_column()
    res = cmp_data[(cmp_data["订单数"] > 10000) & (cmp_data["name"].str.contains("州"))]
    res.reset_index(drop=True, inplace=True)
    res.sort_values(by=['订单数'], ascending=False, inplace=True)


if __name__ == '__main__':
    result = data_add_column()
