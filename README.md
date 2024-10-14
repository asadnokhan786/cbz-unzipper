# cbz-unzipper

## Abstract
- Many individuals who self host comic books or mangas in the .cbz format may occasionally run into performance issues due to the server having to first unzip the comic/manga and then serve the unzipped images to the user. In self hosting situations for large libraries, the bottleneck is more often the image serving speed of the image rather than the available storage space or organization. For this reason, it would be better to store the comics/mangas as unzipped by default on the server from the start, leading to significant performance gain. However unzipping every file can be tedious depending on the scale of the library and having a robust tool that can automatically detect *all* the cbz/rar/zip files in a particular folder and proceed to unzip them into their image form. Enter cbz-unzipper
- cbz-unzipper aims to automate this process of mass conversion of a comic-book/manga library by simply asking the user which folder(s) to detect cbz/rar/zip files from and proceed to unzip them into a new destination folder and cleanup the original folder if the user desires. Listed below is a demonstration of how to use this tool as well as the testing suite guide to check if the tool is working as intended

## TODO
- [x] Create testing suite for basic unzipping functionallity
- [x] Implement unzip feature from source folder to a specifed destination folder of cbz/rar/zip format
- [x] Create testing suite for safety checks
- [ ] Implement safety feature to check if enough storage space exists
- [ ] Implement safety feature in case corrupted zipped files are encountered and contiune to process other files
- [ ] Implement safety feature for persistence in the event user cancels process or computer crashes. Resulting dest folder should contain only fully unzipped/processed files
- [ ] Implement safety feature that doesn't re-unzip/re-process the files that were already unzipped/processed before user cancelation/program failure
- [ ] Create test to confirm logging and dockerization works
- [ ] Implement logging
- [ ] Implement docker contaierization with custom docker image
- [ ] Create test to confirm pdf format conversion feature and revert option works where the unzipped/processed file can be restored to its original format
- [ ] Implement feature that allows user to convert the zipped files to pdf format
- [ ] Implement feature that can convert unzipped/processed files back to their zipped counterparts