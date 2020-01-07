## NPM

See [Learning npm](https://www.linkedin.com/learning/learning-npm-the-node-package-manager-3)

### Node.js on MacOS

- [Node.js](https://nodejs.org/en/download/current/)

To check

`$ node -v`

### VS Code for Mac

- [Visual Studio Code](https://code.visualstudio.com/docs/?dv=osx)

### Useful information

- create package.json: execute `$ npm init`
- add new packages: `npm install <package name>`
- check if dependencies needs to be updated: `npm outdated` or `npm outdated -g`
- to update package `npm update <package name>` or `npm install <package name>`
- remove a package: 
    - *globally*
    
    `sudo npm uninstall <package name> -g`
- *package-lock.json* - a way to control versioning inside of the projects.

When packages are installed globally they can be found in `/usr/local/lib/node_modules`

### Local vs Global installation

- [Guide to NPM](https://blog.bitsrc.io/a-beginners-guide-to-npm-5c021d519c4c)

### Fixing npm permissions

- [Fixing npm permissions](https://github.com/mixonic/docs.npmjs.com/blob/master/content/getting-started/fixing-npm-permissions.md)

### Meaning of versioning

1. `1.4.2` --> exact version; 1 - major release; 4 - minor release; 2 - patch release
2. `^1.x.x` -->  ^ - all minor and patches OK
2. `~1.5.x` -->  ^ - all patches only (See [difference](https://stackoverflow.com/questions/22343224/whats-the-difference-between-tilde-and-caret-in-package-json))

### npm cache

Sometimes npm's cache gets confused

`npm cache verify`

`npm cache clean --force`

### npm audit

- [Auditing package dependencies](https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities)