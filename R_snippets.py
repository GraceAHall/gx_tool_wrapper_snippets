
from Cheetah.Template import Template

rstringarray_snippet = """

## --------- function definition --------- ##

#def text_to_rstringarray($text)
    #set $list = $text.strip().rstrip(',').split(',')

    #set $rstringarray = "c("

    #for $i in range(len($list))
        #set $elem = $list[$i].strip()
        #if $elem != ""
            #set $rstringarray += '"'
            #set $rstringarray += $elem
            #set $rstringarray += '"'
            #if $i != len($list) - 1
                #set $rstringarray += ','
            #end if
        #end if
    #end for

    #set $rstringarray += ')'
    #return $rstringarray
    
#end def

## --------- calling function --------- ##
## when using in a galaxy tool wrapper, pass $param.value to $text_to_rstringarray, rather than just $param. 

Text to R string array example:
#set $my_text_param_value = ", factor xa, thrombin, ,   , trypsin,thermolysin,"
Input text param value:   $my_text_param_value
Output:                   $text_to_rstringarray($my_text_param_value)


"""

t = Template(rstringarray_snippet)
print(t)

