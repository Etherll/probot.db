from distutils.core import setup

with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = 'probot.db',         # How you named your package folder (MyLib)
  packages = ['probot.db'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'probot.db is the best data base ever uses probot database :shitoh:',   # Give a short description about your library
  long_description= long_description,
  author = 'Etherl',                   # Type in your name
  author_email = 'None@domain.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Etherll/OKanime',    # I explain this later on
  keywords = ['ok', 'ok anime', 'anime'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'bs4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
  ],
)
