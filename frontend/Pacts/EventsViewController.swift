//
//  EventsViewController.swift
//  Pacts
//
//  Created by Angela Chen on 8/28/20.
//  Copyright © 2020 Angela Chen. All rights reserved.
//

import UIKit
import SnapKit


class EventsViewController: UIViewController {

    
    var collectionView : UICollectionView!
    
    let padding : CGFloat = 8
    
    // title
    var viewTitle : UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        
        view.backgroundColor = UIColor(red: 250/255, green: 250/255, blue: 250/255, alpha: 1.0)
        viewTitle = UILabel()
        viewTitle.textAlignment = .center
        viewTitle.textColor = UIColor(red: 63/255, green: 63/255, blue: 63/255, alpha: 1.0)
        viewTitle.text = "Upcoming Events"
        viewTitle.font = UIFont.boldSystemFont(ofSize: 30.0)
        view.addSubview(viewTitle)
        
        // Do any additional setup after loading the view.
        
        func setupConstraints() {
            collectionView.snp.makeConstraints { make in
                make.top.equalToSuperview().offset(padding * 13)
                make.leading.equalToSuperview().offset(padding)
                make.trailing.equalToSuperview().offset(-padding)
                make.height.equalTo(6 * padding)
                
            }
            
            viewTitle.snp.makeConstraints { make in
                make.top.equalToSuperview().offset(padding * 7)
                make.centerX.equalTo(view.center.x)
                make.height.equalTo(50)
            }
            
            
        }
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
