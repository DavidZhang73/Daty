model:

```json
{
    "id": Number,
    "name": "", // 128
    "requirement": "", // 300
    "usergroup": ForeignKey,
    "creator": ForeignKey,
    "template_file": File,
    "created_datetime": Datetime,
    "start_datetime": Datetime,
    "end_datetime": Datetime,
}
```



`GET` /api/collection/

parameters:

```json
{
    "serach": "", // name
    "page": "",
    "ordering": "", // created_datetime
}
```

request:

```json
{
}
```

response:

```json
{
    "next": "",
    "prev": "",
    count: Number,
    results: [
        <model>
    ]
}
```

error:

```json
{
}
```



`post` /api/collection/

parameters:

```json
{
}
```

request:

```json
{
    "name": "", // 128
    "requirement": "", // 300
    "usergroup": ForeignKey, // id
    "template_file": File,
    "start_datetime": Datetime,
    "end_datetime": Datetime,
}
```

response:

```json
{
    <model>
}
```

error:

```json
{
}
```



`get` /api/collection/:id

parameters:

```json
{
}
```

request:

```json
{
}
```

response:

```json
{
    <model>
}
```

error:

```json
{
}
```



`put` /api/collection/:id

parameters:

```json
{
}
```

request:

```json
{ 
    "name": "", // 128
    "requirement": "", // 300
    "template_file": File,
    "start_datetime": Datetime,
    "end_datetime": Datetime,
}
```

response:

```json
{
    <model>
}
```

error:

```json
{
}
```



delete` /api/collection/:id

parameters:

```json
{
}
```

request:

```json
{
}
```

response:

```json
{
}
```

error:

```json
{
}
```

status_code:

```json
{
    204: "no content"
}
```

