// const yargs = require('yargs');
// const notes = require('./notes.js');

// Note ekleme komutu

yargs.command({
    command: 'ekle',
    describe: 'Yeni bir not ekle',
    builder: {
        baslik: { demonoption: true, type: 'string', describe: },
        icerik: { demandOption: true, type: 'string', describe:  }
    },
    handler(argv) {
        notes.notEkle(argv.baslik, argv.icerik);
    }
}); 