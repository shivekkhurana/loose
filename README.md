Loose
===================

**Javascript** style objects in **Python**

----------

*JS*

    var helper = {
      url : {
        to : function(slug) {
          return 'http://somesite.com/'+slug ;
        },
        withParams : {
          to : {
            firstModel : function(params) {
              var base='http://somesite.com/firstModel?';
              return URL(base, params);     
            }
          }
        }
      }
    }

> helper.url.to('users') //returns "http://somesite.com/users"

Given a global helper URL that takes a base and queryParams as arguments :
> helper.url.withParams.to.firstModel({page:1}); 
//returns "http://somesite.com/firstModel?page=1"

--------

*Python*

    helper = Loose({
      'url' : Loose({
        'to' : lambda slug (
          'http://somesite.com/'+slug 
        ),
        'withParams' : Loose({
          'to' : Loose({
            'firstModel' : lambda page=1 (
              u = 'http://somesite.com/firstModel?page='
              u + str(page)
            )
          })
        })
      })
    })
    
> helper.url.to('users') //returns "http://somesite.com/users"

Given a global helper URL that takes a base and queryParams as arguments :
> helper.url.withParams.to.firstModel({'page':1}); 
//returns "http://somesite.com/firstModel?page=1"

-------
Installation

`pip install loose`
 
See tests for usage examples.