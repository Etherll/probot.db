# ProBot.DB
### ProBot embed messages feature based database, lol.

Store your data in ProBot database easily, using the embed messages feature, for free :).

## Installation

```sh
pip install probot.db
````

## Usage
Now all you need is a server ID with ProBot, and your auth token from probot.io.
```js
import ProbotDB 

database = ProBotDB('auth token', 'server ID', 'embed name')

database.set('foo', 'bar')
database.get('foo'); // bar
database.push('foo', 'ok')
database.delete('foo');
database.clear();
```
