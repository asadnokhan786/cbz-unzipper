# cbz-unzipper

## Abstract
- Many individuals who self host comic books or mangas in the .cbz format may occasionally run into performance issues due to the server having to first unzip the comic/manga and then serve the unzipped images to the user. In self hosting situations for large libraries, the bottleneck is more often the image serving speed of the image rather than the available storage space or organization. For this reason, it would be better to store the comics/mangas as unzipped by default on the server from the start, leading to significant performance gain. However unzipping every file can be tedious depending on the scale of the library and having a robust tool that can automatically detect *all* the cbz/rar/zip files in a particular folder and proceed to unzip them into their image form. Enter cbz-unzipper
- cbz-unzipper aims to automate this process of mass conversion of a comic-book/manga library by simply asking the user which folder(s) to detect cbz/rar/zip files from and proceed to unzip them into a new destination folder and cleanup the original folder if the user desires. Listed below is a demonstration of how to use this tool as well as the testing suite guide to check if the tool is working as intended

## Use Cases
- In progress :)

## Contributing
- In progress :)

## TODO
- [x] Create testing suite for basic unzipping functionallity
- [x] Implement unzip feature from source folder to a specifed destination folder of cbz/rar/zip format
- [x] Create testing suite for safety checks
- [x] Implement basic cli
- [x] Test basic cli
- [ ] Create tests for zipping feature (default cbz)
- [ ] Implement zipping feature
- [ ] Implement logging feature
- [ ] Test "remember" file creation
- [ ] Implement "remember" file creation
- [ ] Test command flags for advanced customizations
    - [ ] Test global zipping file extension customization
    - [ ] Test exceptions to zipping/unzipping commands to exclude folders/zips
    - [ ] Test verbose cli output
- [ ] Implement command flags for advanced customizations
    - [ ] Implement global zipping file extension customization
    - [ ] Implement exceptions to zipping/unzipping commands to exclude folders/zips
    - [ ] Implement verbose cli output
- [ ] Ensure cli is descriptive in --help
- [ ] Document use cases w/ examples in README.md
- [ ] Document contributing instructions for community