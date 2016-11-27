//
//  ViewController.swift
//  filenameencoder
//
//  Created by 神楽坂雅詩 on 2016/11/27.
//  Copyright © 2016年 KagurazakaYashi. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    
    @IBOutlet weak var option_open: NSSegmentedControl!
    @IBOutlet weak var text_address: NSTextField!
    @IBOutlet weak var btn_browse: NSButton!
    @IBOutlet weak var option_arithmetic: NSSegmentedControl!
    @IBOutlet weak var option_mode: NSSegmentedControl!
    @IBOutlet weak var combo_readencode: NSComboBox!
    @IBOutlet weak var combo_writeencode: NSComboBox!
    @IBOutlet var text_output: NSTextView!
    @IBOutlet weak var btn_preview: NSButton!
    @IBOutlet weak var btn_startrename: NSButton!
    @IBOutlet weak var btn_exit: NSButton!
    
    @IBAction func btn_browse_a(_ sender: NSButton) {
    }
    
    @IBAction func option_arithmetic_a(_ sender: NSSegmentedControl) {
    }
    
    @IBAction func btn_preview_a(_ sender: NSButton) {
    }
    
    @IBAction func btn_startrename_a(_ sender: NSButton) {
    }
    
    @IBAction func btn_exit_a(_ sender: NSButton) {
        exit(0)
    }
    
    let cp_py = Bundle.main.path(forResource: "filenameencoder", ofType: "py")!

    override func viewDidLoad() {
        super.viewDidLoad()
        print(cp_py)
        //selfcheck()
    }
    
    func selfcheck() {
        let result = runCommand(arguments: ["-h","cn"])
        print(result)
    }
    
    func runCommand(arguments: [String]) -> String {
        let pipe = Pipe()
        let file = pipe.fileHandleForReading
        let ntask = Process()
        ntask.launchPath = cp_py
        ntask.arguments = arguments
        ntask.standardOutput = pipe
        ntask.launch()
        let data = file.readDataToEndOfFile()
        return String(data: data, encoding: String.Encoding.utf8)!
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

