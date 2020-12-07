# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

+ colored trees
+ add more field designs (circle, diamond, random)
+ add more tree design
+ input fixed size as parameters

## 0.4 - 2020-12-02

### Changed

+ formula of max number of trees, now depends on field and tree surfaces and occupation rate coefficient
+ case for constants into capital

### Added

+ comments detailing the formula of maximum number of trees

## 0.3 - 2020-11-23

### Fixed

+ module docstring typo

### Removed

+ unused math and iterator imports

### Changed

+ list comprehension indexed iterators
+ max number of trees formula, simpler now
+ method to get tree random positions, only sort list of y positions
+ planting for loop in accordance to previous point
+ random range call

### Added

+ more comments

## 0.2 - 2020-11-22

### Fixed

+ tree position ordering was not saved, thus persepective was not rendered properly

### Changed

+ constants defined in script scope
+ more constants naming and less magic numbers

## 0.1 - 2020-11-22

### Added

+ get a single random place
+ place only tree trunks
+ place trees wholy
+ get several random places
+ do perspective
