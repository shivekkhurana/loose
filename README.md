Loose
===================

**Javascript** style objects in **Python**

----------

Loose() is a way to add expressive power to plain old python dicts. It is inspired by JavaScript objects : 

*JS Object*

    var helper = {
      url : {
        to : function(slug) {
          return 'http://somesite.com/'+slug ;
        }
      }
    }

> helper.url.to('users') 

`returns "http://somesite.com/users"`

----
*Loose Object in python*

####Basic use case
    helper = Loose({
      'url' : Loose({
        'to' : lambda slug: (
          'http://somesite.com/'+slug 
        )
      })
    })
    
> \>\>\> helper.url.to('users') 

`returns "http://somesite.com/users"`


-------

####Using the `default` method
    helper = Loose({
      'url' : Loose({
        'default' : 'http://somesite.com',
        'to' : lambda slug: (
          'http://somesite.com/'+slug 
        )
      })
    })
    
> \>\>\> helper.url()

`returns "http://somesite.com"`

-------
####Installation

`pip install loose`

-------
####Issue Tracking and Bug Reports
Add that shit to github's issue tracker.