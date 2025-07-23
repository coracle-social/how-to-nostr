<?php

return [
    /**
     * The book title.
     */
    'title' => 'Building Nostr',

    /**
     * The author name.
     */
    'author' => 'hodlbod',

    /**
     * The list of fonts to be used in the different themes.
     */
    'fonts' => [
         'lato' => 'Lato-Regular.ttf',
    ],

    /**
     * Document Dimensions.
     */
    'document' => [
        'format' => [210, 297],
        'margin_left' => 27,
        'margin_right' => 27,
        'margin_bottom' => 14,
        'margin_top' => 14,
    ],

    /**
     * Table of Contents Levels
     */
    'toc_levels' => [
        'H1' => 0,
        'H2' => 0,
        'H3' => 1,
    ],

    /**
     * Cover photo position and dimensions
     */
    'cover' => [
        'position' => 'position: absolute; left:0; right: 0; top: -.2; bottom: 0;',
        'dimensions' => 'width: 210mm; height: 297mm; margin: 0;',
        'image' => 'cover.png',
    ],

    /**
     * Page ranges to be used with the sample command.
     */
    'sample' => [
        [1, 7],
        [15, 15],
    ],

    /**
     * default commonmark
     */
    'configure_commonmark' => [
    ],
    /**
     * A notice printed at the final page of a generated sample.
     */
    'sample_notice' => 'If you enjoyed this book, consider <a href="https://geyser.fund/project/buildingnostr">donating</a>.',

    /**
     * CSS inline style for the page header.
     * If you want to skip header, comment the line
     */
    'header' => 'font-style: italic; text-align: right; border-bottom: solid 1px #808080;',

    /**
     * List of the Markdown files.
     * If the `md_file_list` is not set (default)
     * all the markdown files in the content directory
     * will be loaded.
     * If you need to select a subset of markdown files
     * for creating PDF or EPUB or HTML you can list here
     * the files. You need to set the filename in the
     * content directory. The fieldname should include the
     * extension.
     */
    /*
        'md_file_list' => [
            'routing.md',
            'artisan.md',
            'console-tests.md',
        ],
    */
];
