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
        
        tabBar.barTintColor = UIColor(red: 244/255, green: 244/255, blue: 244/255, alpha: 1.0)
        tabBar.tintColor = UIColor(red: 183/255, green: 65/255, blue: 136/255, alpha: 1.0)
        tabBar.isTranslucent = false
        // Do any additional setup after loading the view.
        
        let EViewController = EventsViewController()
        EViewController.tabBarItem = UITabBarItem(title: "", image: UIImage(named: "event"), selectedImage: UIImage(named: "SelectedEvent"))
               
        let PViewController = PactsViewController()
        PViewController.tabBarItem = UITabBarItem(title: "", image: UIImage(named: "greyEvent"), selectedImage: UIImage(named: "SelectedPacts"))
        
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
