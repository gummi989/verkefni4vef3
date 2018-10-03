<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>JSON API</title>
    <link rel="stylesheet" href="/static/main.css">
</head>
<body>
    % include("header.tpl")
    <section>
        <h2>Currency exchange rates in relation to ISK (apis.is)</h2>
        <table>
            <thead>
                <tr>
                    <th>Long name</th>
                    <th>Short name</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                % for currency in e_rate["results"]:
                    <tr>
                        <td>{{currency["longName"]}}</td>
                        <td>{{currency["shortName"]}}</td>
                        <td>{{currency["value"]}}</td>
                    </tr>
                % end
            </tbody>
        </table>
    </section>
    % include("footer.tpl")
</body>
</html>
