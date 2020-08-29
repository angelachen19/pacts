//
//  EventsTableTableViewController.swift
//  Pacts
//
//  Created by Angela Chen on 8/28/20.
//  Copyright © 2020 Angela Chen. All rights reserved.
//

import UIKit

class EventsTableTableViewController: UITableViewController {

    @IBOutlet weak var EventImageView: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem
    }


    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 0
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "EventsIdentifier", for: indexPath)
        return cell
    }


}
