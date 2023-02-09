# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Version 0.1.0] - 2023-02-09
### Added
- Error handling for incorrect URL format: To ensure the program can handle incorrect URL format and provide a clear error message to the user, the input URL format was validated using regular expressions.

I wanted to add error handling for the input URL format for several reasons:

- User Experience: Without proper validation of the URL format, the program may fail or produce unexpected results if the user provides an incorrect URL. By adding error handling for the URL format, the program can inform the user about the issue and ask for a valid URL, which will improve the overall user experience.
- Debugging: By validating the URL format, it is easier to identify and debug any issues that might occur. This is because a well-defined error message can be provided to the user, which will help in diagnosing the problem and fixing it.
- Security: Incorrectly formatted URLs can pose a security risk to the program. For example, a malicious user could provide an URL that contains a script that can compromise the security of the program or the system it is running on. By validating the URL format, the program can reduce the risk of such attacks.

In conclusion, adding error handling for the input URL format is important for improving the user experience, facilitating debugging, and enhancing the security of the program.


## [Unreleased]

## [Version X.Y.Z] - YYYY-MM-DD
### Added
- Feature X: Brief description of the new feature and its purpose

### Changed
- Feature Y: Brief description of the changes made to the existing feature and its impact

### Fixed
- Bug Z: Brief description of the bug that was fixed and how it was fixed

### Removed
- Feature W: Brief description of the feature that was removed and the reason for its removal

### Security
- Vulnerability P: Brief description of the security vulnerability that was fixed and its impact