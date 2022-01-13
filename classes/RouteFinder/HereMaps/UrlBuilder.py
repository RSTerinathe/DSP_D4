def buildUrl(base_url, route, parameters):
    url = base_url + route
    # Check if we need to add any parameters
    if parameters:
        url += '?'
        for key, value in parameters.items():
            if isinstance(value, list):
                value = ";".join(value)
            url += f"&{key}={value}"
    return url
