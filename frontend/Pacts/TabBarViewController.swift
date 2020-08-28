//
//  TabBarViewController.swift
//  Pacts
//
//  Created by Angela Chen on 8/27/20.
//  Copyright © 2020 Angela Chen. All rights reserved.
//

import UIKit

class TabBarViewController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()
        //color of the bottom bar-slight gray
        tabBar.barTintColor = UIColor(red: 244/255, green: 244/255, blue: 244/255, alpha: 1.0)
        //color icons when selected
        tabBar.tintColor = UIColor(red: 63/255, green: 63/255, blue: 63/255, alpha: 0.7)
        tabBar.isTranslucent = false
        // Do any additional setup after loading the view.
        
        let EViewController = EventsViewController()
        EViewController.tabBarItem = UITabBarItem(title: "", image: UIImage(named: "Event"), selectedImage: UIImage(named: "SelectedEvent"))
               
        let PViewController = PactsViewController()
        PViewController.tabBarItem = UITabBarItem(title: "", image: UIImage(named: "Pacts"), selectedImage: UIImage(named: "SelectedPacts"))
        
        let tabBarList = [EViewController, PViewController]
        
        viewControllers = tabBarList
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
